import "./main.scss";
import Alpine from "alpinejs";
import "./htmx.js";
import ApexCharts from "apexcharts";

import "../../util-js/dropdown.js";
import "../../partials/home/add-debt-modal/add-debt-modal.js";
import "../../partials/home/dashboard/dashboard.js";
import "../../partials/home/menu/menu-desktop/sidebar.js";
import "../../partials/home/dashboard/components/chart/chart-control.js";
import "../../partials/home/transactions/transactions.js";
import "../../partials/home/wallet/wallet.js";
import "../../partials/home/ajusts/ajusts.js";
import "../../partials/home/menu/navbar/components/notifications/notification.js";
import "../../partials/home/bubble/bubble-control.js";
import "../../partials/home/dashboard/components/chart-monthly-evolution/chart.js";
import "../../partials/home/wallet/components/modal/components/chart/chart.js";

window.Alpine = Alpine;
Alpine.start();

Alpine.data("themeControl", () => ({
    currentTheme: localStorage.getItem("theme") || "default",

    init() {
        document.body.setAttribute("data-theme", this.currentTheme);
    },

    toggleTheme() {
        this.currentTheme =
            this.currentTheme === "default" ? "dark" : "default";
        document.body.setAttribute("data-theme", this.currentTheme);
        localStorage.setItem("theme", this.currentTheme);
    },
}));

window.addEventListener('DOMContentLoaded', () => {
  const sidebar = document.querySelector('.sidebar');
  if (sidebar.classList.contains('no-transition')) {
    requestAnimationFrame(() => {
      sidebar.classList.remove('no-transition');
    });
  }
});