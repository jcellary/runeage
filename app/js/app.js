'use strict';


// Declare app level module which depends on filters, and services
angular.module('runeAge', [
    'ngRoute',
    'runeAge.filters',
    'runeAge.services',
    'runeAge.directives',
    'runeAge.controllers'
]).
config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/welcome', {templateUrl: 'partials/welcome.html', controller: 'WelcomeCtrl'});
    $routeProvider.when('/game', {templateUrl: 'partials/game.html', controller: 'GameCtrl'});
    $routeProvider.otherwise({redirectTo: '/welcome'});
}]);
