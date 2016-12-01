app
    .controller('BancoCtrl', function($scope, $state, $stateParams,
        asociacionService, $window, $mdDialog, $log, toastr) {
        $scope.fields = 'numero';
        var params = {};
        $scope.lista = [];
        $scope.banco = {
            name: 'Banco',
            detail_name: 'Trabajar con entidad bancaria',
            version: 'v1.0',
        };

        $scope.list = function(params) {
            $scope.isLoading = true;
            asociacionService.CuentaBanco.query(params, function(r) {
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
                asociacionService.CuentaBanco.delete({ id: d.id }, function(r) {
                    $log.log("Se eliminó la entidad bancaria:" + JSON.stringify(d));
                    toastr.success('Se eliminó la entidad bancaria ' + d.ruc, 'Banco');
                    $scope.list(params);
                }, function(err) {
                    $log.log("Error in delete:" + JSON.stringify(err));
                    toastr.error(err.data.detail, err.status + ' ' + err.statusText);
                });
            }
        };
    })
    .controller("BancoSaveCtrl", function($scope, $state, $stateParams,
        asociacionService, $window, $mdDialog, $log, toastr) {
        //Valores iniciales
        $scope.banco = {
            name: 'Banco',
            detail_name: 'Agregando entidad bancaria',
            version: 'v1.0',
        };

        $scope.sel = function() {
            asociacionService.CuentaBanco.get({ id: $stateParams.id }, function(r) {
                $scope.banco = r;
            }, function(err) {
                $log.log("Error in get:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        };
        if ($stateParams.id) {
            $scope.sel();
        }

        $scope.save = function() {
            if ($scope.banco.id) {
                asociacionService.CuentaBanco.update({ id: $scope.banco.id }, $scope.banco, function(r) {
                    $log.log("r: " + JSON.stringify(r));
                    toastr.success('Se editó la entidad bancaria ' + r.nombre, 'Banco');
                    $state.go('asociacion.asociacion.banco');
                }, function(err) {
                    $log.log("Error in update:" + JSON.stringify(err));
                    toastr.error(err.data.detail, err.status + ' ' + err.statusText);
                });
            } else {
                asociacionService.CuentaBanco.save($scope.banco, function(r) {
                    $log.log("r: " + JSON.stringify(r));
                    toastr.success('Se insertó la entidad bancaria ' + r.nombre, 'Banco');
                    $state.go('asociacion.asociacion.banco');
                }, function(err) {
                    $log.log("Error in save:" + JSON.stringify(err));
                    toastr.error(err.data.detail, err.status + ' ' + err.statusText);
                });
            }
        };

        $scope.cancel = function() {
            $state.go('asociacion.asociacion.banco');
        };
    });
