var dp = new DayPilot.Scheduler("dp");
dp.init();

function loadResources() {
  dp.rows.load("flask.py");
}

function loadEvents() {
  dp.events.load("backend_events.php"); //This will input JSON code blocks for each person
}

var dp = new DayPilot.Scheduler("dp");
dp.init();

loadResources();
