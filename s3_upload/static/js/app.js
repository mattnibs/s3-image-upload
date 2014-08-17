'use strict';

angular.module('app', ['app.directives'])

// fix for getting django/angular mustaches to jive
.config(function($interpolateProvider) {
    	$interpolateProvider.startSymbol('{$');
    	$interpolateProvider.endSymbol('$}');
	})

.controller('TestUploadCtrl', ['$scope', '$http',
    function($scope, $http) {

        $scope.UploadImage = function () {

            // set loading state
            $scope.loading = true;

            // construct form data from image
            var fd = new FormData();
            fd.append('file', $scope.image);

            // send out to server
            $http.post('/api/images/', fd, {
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined}
            })
            .success(function(data) {
                $scope.imagePostResponse = data;
                console.log(data); // so you can view the response in your console
            })
            .error(function(data) {
                $scope.imagePostResponse = data;
                console.log(data); // ditto the above
            })
            .finally(function() { $scope.loading = false; }); // turn off loading state


        };
    }
])

.controller('TestGetCtrl',
    function (){
        // do nothing
    }
);
