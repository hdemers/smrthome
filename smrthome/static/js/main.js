/* Author: Hugues Demers
 * Copyrights 2013
*/
require({
  baseUrl: "static/js",
  paths: {
    "jquery": "other/jquery-1.9.1.min",
    "knockout": "other/knockout-2.2.1",
    "underscore": "other/underscore-min",
    "domReady": "other/domReady",
    "bootstrap": "other/bootstrap.min",
    "moment": "other/moment.min",
    "d3": "other/d3.v3"
  },
  shim: {
    'underscore': {
      exports: '_'
    },
    'knockout': {
      exports: 'ko'
    },
    'moment': {
      exports: 'moment'
    },
    'd3': {
      exports: 'd3'
    },
    'bootstrap': {
      exports: 'bootstrap',
      deps: ['jquery']
    }
  }
});

require(['domReady', 'app'],
function (domReady, app) {
  domReady(function () {
    console.log("DOM ready.");
    app.initialize();
  });
});


