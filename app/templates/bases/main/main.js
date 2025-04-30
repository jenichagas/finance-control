import "./main.scss";
import Alpine from "alpinejs";
import "./htmx.js"

import "../../partials/home/add-debt-modal/components/dropdown.js";
import "../../partials/home/add-debt-modal/add-debt-modal.js";
import "../../partials/home/dashboard/dashboard.js";
import "../../partials/home/menu/menu-desktop/sidebar.js";


window.Alpine = Alpine;
Alpine.start();

Alpine.data('themeControl', () => ({
    currentTheme: localStorage.getItem("theme") || "default",
    
    init() {
      document.body.setAttribute("data-theme", this.currentTheme);
    },
    
    toggleTheme() {
      this.currentTheme = this.currentTheme === 'default' ? 'dark' : 'default';
      document.body.setAttribute("data-theme", this.currentTheme);
      localStorage.setItem("theme", this.currentTheme);
    }
  }));