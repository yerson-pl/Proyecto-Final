app
    .controller('AsociacionCtrl', function($scope, $state, $stateParams,
        asociacionService, $window, $mdDialog, $log, toastr) {
        $scope.fields = 'ruc, name';
        var params = {};
        $scope.lista = [];
        $scope.asociacion = {
            name: 'Asociacion',
            detail_name: 'Trabajar con asociacion',
            version: 'v1.0',
        };

        $scope.list = function(params) {
            $scope.isLoading = true;
            asociacionService.Asociacion.query(params, function(r) {
                $scope.lista = r;
                $scope.isLoading = false;
            }, function(err) {
                $log.log("Error in list:" + JSON.stringify(err));
                toastr.error(err.data.results.detail, err.status + ' ' + err.statusText);
            });
        };

        $scope.list(params);

     /*   $scope.listCuentaBanco = function(i) {
            asociacionService.CuentaBanco.list({ cuenta_banco: i }).$promise.then(function(r) {
                $scope.listaCuentaBanco = r;
            }, function(err) {
                console.log("Err " + err);
            });
        };

        $scope.listCuentaBanco();*/

        $scope.buscar = function() {
            params.page = 1;
            params.fields = $scope.fields;
            params.query = $scope.query;
            $scope.list(params);
        };

        $scope.onReorder = function(order) {
            //Todo
            $log.log('Order: ' + order);
        };

        $scope.delete = function(d) {
            if ($window.confirm("Seguro?")) {
                asociacionService.Asociacion.delete({ id: d.id }, function(r) {
                    $log.log("Se eliminó la asociacion:" + JSON.stringify(d));
                    toastr.success('Se eliminó la asociacion ' + d.ruc, 'Asociacion');
                    $scope.list(params);
                }, function(err) {
                    $log.log("Error in delete:" + JSON.stringify(err));
                    toastr.error(err.data.detail, err.status + ' ' + err.statusText);
                });
            }
        };
    })
    .controller("AsociacionSaveCtrl", function($scope, $state, $stateParams,
        asociacionService, $window, $mdDialog, $log, toastr) {
        //Valores iniciales
        $scope.asociacion = {};

        $scope.sel = function() {
            asociacionService.Asociacion.get({ id: $stateParams.id }, function(r) {
                $scope.asociacion = r;
            }, function(err) {
                $log.log("Error in get:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        };
        if ($stateParams.id) {
            $scope.sel();
        }

        $scope.save = function() {
            if ($scope.asociacion.id) {
                asociacionService.Asociacion.update({ id: $scope.asociacion.id }, $scope.asociacion, function(r) {
                    $log.log("r: " + JSON.stringify(r));
                    toastr.success('Se editó la asociacion ' + r.nombre, 'Asociacion');
                    $state.go('asociacion.asociacion.asociacion');
                }, function(err) {
                    $log.log("Error in update:" + JSON.stringify(err));
                    toastr.error(err.data.detail, err.status + ' ' + err.statusText);
                });
            } else {
                asociacionService.Asociacion.save($scope.asociacion, function(r) {
                    $log.log("r: " + JSON.stringify(r));
                    toastr.success('Se insertó la asociacion ' + r.nombre, 'Asociacion');
                    $state.go('asociacion.asociacion.asociacion');
                }, function(err) {
                    $log.log("Error in save:" + JSON.stringify(err));
                    toastr.error(err.data.detail, err.status + ' ' + err.statusText);
                });
            }
        };

        $scope.cancel = function() {
            $state.go('asociacion.asociacion.asociacion');
        };
    });
