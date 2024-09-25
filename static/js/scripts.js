// scripts.js
document.addEventListener("DOMContentLoaded", function () {
  // Rotational Speed vs Torque Chart
  var options1 = {
    chart: {
      type: "line",
      height: 300,
      background: "#1F1F1F",
    },
    series: [
      {
        name: "Rotational Speed (RPM)",
        data: [1500, 1600, 1550, 1700, 1650],
      },
      {
        name: "Torque (Nm)",
        data: [50, 60, 55, 70, 65],
      },
    ],
    xaxis: {
      categories: ["Jan", "Feb", "Mar", "Apr", "May"],
      labels: {
        style: {
          colors: "#E0E0E0",
        },
      },
    },
    yaxis: {
      labels: {
        style: {
          colors: "#E0E0E0",
        },
      },
    },
    theme: {
      mode: "dark",
    },
    colors: ["#00D1FF", "#FFA600"],
  };

  var chart1 = new ApexCharts(
    document.querySelector("#rotationalSpeedVsTorqueChart"),
    options1
  );
  chart1.render();

  // Temperature Trends Chart
  var options2 = {
    chart: {
      type: "bar",
      height: 300,
      background: "#1F1F1F",
    },
    series: [
      {
        name: "Air Temperature",
        data: [30, 32, 31, 33, 34],
      },
      {
        name: "Process Temperature",
        data: [75, 78, 76, 80, 79],
      },
    ],
    xaxis: {
      categories: ["Jan", "Feb", "Mar", "Apr", "May"],
      labels: {
        style: {
          colors: "#E0E0E0",
        },
      },
    },
    yaxis: {
      labels: {
        style: {
          colors: "#E0E0E0",
        },
      },
    },
    theme: {
      mode: "dark",
    },
    colors: ["#00D1FF", "#FFA600"],
  };

  var chart2 = new ApexCharts(
    document.querySelector("#temperatureTrendsChart"),
    options2
  );
  chart2.render();

  // Feature Importance Chart
  var options4 = {
    chart: {
      type: "radar",
      height: 300,
      background: "#1F1F1F",
    },
    series: [
      {
        title: "Feature Importance",
        name: "Feature Importance",
        data: [376, 264, 308, 224, 303, 254, 376, 68, 47],
      },
    ],
    labels: [
      "Power",
      "Temperature Diff",
      "Rotational Speed",
      "Air Temperature",
      "Torque",
      "Process Temperature",
      "Tool Wear",
      "Type L",
      "Type M",
    ],
    theme: {
      mode: "dark",
    },
    colors: ["#00D1FF"],
  };

  var chart4 = new ApexCharts(
    document.querySelector("#featureImportanceChart"),
    options4
  );
  chart4.render();
});
