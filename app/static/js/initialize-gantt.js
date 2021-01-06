let data = [
  {
    recordID: 1,
    row: "Row for ID #1",
    start: "Wed Jun 03 2020 14:21:55",
    end: "Wed Jun 03 2020 20:21:55",
  },
  {
    recordID: 2,
    row: "Row for ID #2",
    start: "Jun 03 2020 11:00:00",
    end: "Jun 03 2020 15:23:43",
  },
  {
    recordID: 1,
    row: "Row for ID #1",
    start: "Wed Jun 03 2020 06:00:00",
    end: "Wed Jun 03 2020 10:00:00",
  },
  {
    recordID: 5,
    row: "Now we have grouping",
    start: "Wed Jun 03 2020 06:00:00",
    end: "Wed Jun 03 2020 10:00:00",
  },
];

//This could be an API call to grab data
function refreshFunction() {
  return data;
}

//Parameters that the chart expects
let params = {
  sidebarHeader: "Unused right now",
  noDataFoundMessage: "No data found",
  startTimeAlias: "start",
  endTimeAlias: "end",
  idAlias: "recordID",
  rowAlias: "row",
  linkAlias: null,
  refreshFunction: refreshFunction,
};

//Create the chart.
//On first render the chart will call its refreshData function on its own.
let ganttChart = new Gantt("chart", params);

//To refresh the chart's data
ganttChart.refreshData();