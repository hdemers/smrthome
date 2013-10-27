/* Author: Hugues Demers
 * Copyrights 2013
  
*/
define([
  "jquery",
  "underscore",
  "knockout",
  "viewmodel",
  "moment"
],
function ($, _, ko, viewmodel, moment) {
  var exports = {};

  exports.initialize = function () {
    console.log("Initializing 'birdwatch' app.");
    ko.applyBindings(viewmodel);
  };


  return exports;
});
