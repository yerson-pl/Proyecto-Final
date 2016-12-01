var eventosUrl = 'http://localhost:9000/api/eventos/';

var config = {

    eventosUrl: eventosUrl,


};

app

    .value('configEventos', config);

app.constant('ROUTERS3', {
    "xxxx": {
        "url": "/xxx",
        "templateUrl": "templates/xxx.html"
    },
    "eventos": {
        "url": "/eventos",
        "views": {
            "": {
                "templateUrl": "app/views/layout.html"
            },
            "aside": {
                "templateUrl": "app/views/aside.html"
            },
            "content": {
                "templateUrl": "app/views/content.html"
            }
        }
    },
      "eventos.eventos": {
        "url": "/eventos",
        "template": "<div ui-view ></div>"
    },

    "eventos.eventos.eventos": {
        "url": "/list",
        "data": {
            "section": "Eventos",
            "page": "Eventons"
        },
        "templateUrl": "americas_web_apps/eventos_web/views/eventos/index.html"
    },
    "eventos.eventos.eventoNew": {
        "url": "/new",
        "data": {
            "section": "Eventos",
            "page": "Evento"
        },
        "templateUrl": "americas_web_apps/eventos_web/views/eventos/form.html"
    },
    "eventos.eventos.eventoEdit": {
        "url": "/eventos/:id/edit",
        "data": {
            "section": "Eventos",
            "page": "Evento"
        },
        "templateUrl": "americas_web_apps/eventos_web/views/eventos/form.html"
    },
    "eventos.eventos.eventoAsistencia": {
        "url": "/eventos/:id/registro",
        "data": {
            "section": "Eventos",
            "page": "Evento"
        },
        "templateUrl": "americas_web_apps/eventos_web/views/eventos/formlist.html"
    },
      "eventos.eventos.asistencias": {
        "url": "/asistencias",
        
        "templateUrl": "americas_web_apps/eventos_web/views/asistencias/index.html"
    },
    "eventos.eventos.asistenciaNew": {
        "url": "/newadd",
        "data": {
            "section": "Eventos",
            "page": "Evento"
        },
        "templateUrl": "americas_web_apps/eventos_web/views/asistencias/form.html"
    },

});