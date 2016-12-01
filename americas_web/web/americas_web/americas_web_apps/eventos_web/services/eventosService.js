app

    .factory("eventosService", function($resource, configEventos) {
    var url = configEventos.eventosUrl;
    return {

        Evento: $resource(url + "eventos/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },
        }),
        Asistencia: $resource(url + "asistencias/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },
        }),


    };
});
