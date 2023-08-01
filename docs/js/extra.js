// this is a javascript to build out default datatables in markdown.
document$.subscribe(function() {
    var tables = document.querySelectorAll("article table:not([class])")
    tables.forEach(function(table) {
      $(table).DataTable();
    });
  });