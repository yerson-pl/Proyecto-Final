app.controller("EventoCtrl", function($scope, $state, $stateParams, eventosService, $window, $mdDialog, $log, toastr) {

        $scope.lista = [];

        $scope.list = function() {
            eventosService.Evento.query(function(r) {
                $scope.lista = r;
            });
        };

        $scope.delete = function(e) {
            eventosService.Evento.delete({ id: e.id }, function(r) {
                $scope.list();
            });
        };

        $scope.list();

    })
    .controller("EventoSaveCtrl", function($scope, eventosService, $state, $stateParams) {
        $scope.evento = {};

        $scope.sel = function() {
            eventosService.Evento.get({ id: $stateParams.id }, function(r) {
                $scope.evento = r;
            });
        };

        if ($stateParams.id) {
            $scope.sel();
        }

        $scope.save = function() {
            if ($scope.evento.id) {
                eventosService.Evento.update({ id: $scope.evento.id }, $scope.evento, function(r) {
                    $state.go('eventos.eventos.eventos');
                });
            } else {
                eventosService.Evento.save($scope.evento, function(r) {
                    $state.go('eventos.eventos.eventos');
                });
            }

        };

        $scope.cancel = function() {
            $state.go('eventos.eventos.eventos');
        };

    });
