//subscribes to jquery library
//searches for elements in the site that have a table
//applies the default datatables library to these elements
document$.subscribe(function() {
    var tables = document.querySelectorAll("article table:not([class])")
    tables.forEach(function(table) {
      $(table).DataTable();
    });
  });