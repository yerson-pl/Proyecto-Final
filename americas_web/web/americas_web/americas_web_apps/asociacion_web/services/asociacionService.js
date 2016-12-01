app
    .factory('asociacionService', function($resource, configAsociacion) {

        var url = configAsociacion.asociacionUrl;

        return {
            Asociacion: $resource(url + "asociacion/:id/", { 'id': '@id' }, {
                "update": { method: 'PUT' },
            }),
            CuentaBanco: $resource(url + "banco/:id/", { 'id': '@id' }, {
                "update": { method: 'PUT' },
            }),
        };
    });
