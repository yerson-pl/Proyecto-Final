app.controller("AsistenciaCtrl", function($scope, $state, $stateParams, eventosService, $window, $mdDialog, $log, toastr) {

    $scope.lista = [];

    $scope.list = function() {
        eventosService.Asistencia.query(function(r) {
            $scope.lista = r;
        });
    };

});
