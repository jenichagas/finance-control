from fastapi import APIRouter, Query
from app.config.mongodb import db
from app.models.debt import Debt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from app.models.debt_update import DebtUpdate
from fastapi import HTTPException
from bson import ObjectId
from app.routers.debt_categories import CATEGORIES


router = APIRouter()


@router.post("/debt")
async def create_debt(debt: Debt):
    installments = []
    base_value = round(debt.value / debt.installments, 2)
    total = base_value * debt.installments
    diff = round(debt.value - total, 2)

    for i in range(debt.installments):
        ref_date = debt.start_date + relativedelta(months=i)

        value = base_value + diff if i == debt.installments - 1 else base_value

        installments.append(
            {
                "name": debt.name,
                "category": debt.category,
                "value": value,
                "installments": f"{i+1}/{debt.installments}",
                "reference_month": f"{ref_date.year}-{ref_date.month:02}",
                "original_start_date": debt.start_date.isoformat(),
            }
        )

    result = await db.debts.insert_many(installments)
    new_debts = await db.debts.find({"_id": {"$in": result.inserted_ids}}).to_list(
        length=debt.installments
    )
    return [{**d, "_id": str(d["_id"])} for d in new_debts]


@router.get("/debt/by-month")
async def get_debts_by_month(month: str = Query(..., example="2025-04")):
    dbts = await db.debts.find({"reference_month": month}).to_list(1000)
    return [{**d, "_id": str(d["_id"])} for d in dbts]


@router.get("/debt/total-by-month")
async def get_total_by_month(month: str = Query(..., example="2025-04")):

    cursor = db.debts.aggregate(
        [
            {"$match": {"reference_month": month}},
            {"$group": {"_id": None, "total": {"$sum": "$value"}}},
        ]
    )
    result = await cursor.to_list(1)
    total = result[0]["total"] if result else 0
    return {"month": month, "total": total}


@router.get("/debt/by-category")
async def get_debts_grouped_by_category(month: str = Query(..., example="2025-04")):

    cursor = db.debts.aggregate(
        [
            {"$match": {"reference_month": month}},
            {"$group": {"_id": "$category", "total": {"$sum": "$value"}}},
        ]
    )
    result = await cursor.to_list(length=100)
    return [{"category": doc["_id"], "total": doc["total"]} for doc in result]


@router.delete("/debt/{id}")
async def delete_debt(id: str):
    result = await db.debts.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Dívida não encontrada")
    return {"status": "deleted", "id": id}


@router.put("/debt/{id}")
async def update_debt(id: str, debt_data: DebtUpdate):
    updated_data = debt_data.model_dump(exclude_unset=True)
    result = await db.debts.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    return {"status": "updated", "id": id, "updated_fields": updated_data}


@router.get("/debt/categories")
async def get_categories():
    return CATEGORIES
