import Alpine from "alpinejs";
import ApexCharts from "apexcharts";

const chartControl = () => ({
    chart: null,

    init() {
        const options = {
            series: [44, 55, 41, 17, 15],
            chart: {
                width: 380,
                type: "donut",
            },
            plotOptions: {
                pie: {
                    startAngle: -90,
                    endAngle: 270,
                },
            },
            dataLabels: {
                enabled: false,
            },
            fill: {
                type: "gradient",
            },
            legend: {
                formatter: function (val, opts) {
                    return (
                        val + " - " + opts.w.globals.series[opts.seriesIndex]
                    );
                },
            },
            title: {
                text: "",
            },
            responsive: [
                {
                    breakpoint: 480,
                    options: {
                        chart: {
                            width: 200,
                        },
                        legend: {
                            position: "bottom",
                        },
                    },
                },
            ],
        };

        this.chart = new ApexCharts(
            document.getElementById("column-chart"),
            options
        );
        this.chart.render();
    },

    destroy() {
        if (this.chart) {
          this.chart.destroy();
        }
      },
});

Alpine.data("chartControl", chartControl);
