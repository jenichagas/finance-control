import Alpine from "alpinejs";
import ApexCharts from "apexcharts";

const categoryComparisonChart = () => ({
    chart: null,

    init () {
        const options = {
            chart: {
                type: "bar",
                height: 300,
            },
            series: [
                {
                    name: "Mês Atual",
                    data: [900, 1150, 750, 400], 
                },
                {
                    name: "Mês Anterior",
                    data: [850, 950, 600, 300], 
                },
            ],
            xaxis: {
                categories: ["Alimentação", "Transporte", "Lazer", "Educação"],
          
            },
            colors: ["#2ed8b6", "#f06543"],
            plotOptions: {
                bar: {
                    columnWidth: "45%",
                },
            },
            stroke: {
                width: 1,
                colors: ["#fff"]
            },
            dataLabels: {
                enabled: false
            },
            legend: {
                position: 'bottom',
                horizontalAlign: 'right'
            },
            tooltip: {
                y: {
                    formatter: (val) => `R$ ${val.toFixed(2)}`
                }
            }
        };


        this.chart = new ApexCharts(
            document.getElementById("chart-comparison"),
            options
        );
        this.chart.render();
    },
    
});


Alpine.data("categoryComparisonChart", categoryComparisonChart);
