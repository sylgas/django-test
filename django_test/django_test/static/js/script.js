(function () {
    var app;

    app = angular.module('django_test.person_connection', []);

    app.controller('PersonController', function ($scope, $http) {
            $scope.person_list = [];
            $scope.showDetails = function (person) {
                $scope.connections = [];
                return $http.get('/api/person/'+ person.id +'/connection').then(function (result) {
                    return angular.forEach(result.data, function (item) {
                        return $scope.connections.push(item);
                    });
                });
            }

            return $http.get('/api/person').then(function (result) {
                return angular.forEach(result.data, function (item) {
                    return $scope.person_list.push(item);
                });
            });
        }
    );



}).call(this);

(function () {
    var app;

    app = angular.module('django_test.create_person', ['ngResource']);

    app.config(['$httpProvider', function ($httpProvider) {
            $httpProvider.defaults.headers.common['X-CSRFToken'] = '{{ csrf_token|escapejs }}';
        }]);

    app.factory('CallPerson', [
        '$resource', function ($resource) {
            return $resource('/api/person/create');
        }
    ]);

    app.controller('CreateController', [
        '$scope', 'CallPerson', function ($scope, CallPerson) {
            $scope.newPerson = new CallPerson();
            return $scope.save = function () {
                return CallPerson.save($scope.newPerson, function (result) {
                    $scope.newPerson = new CallPerson();
                    return $scope.person_list.push(result);
                });
            };
        }
    ]);

}).call(this);