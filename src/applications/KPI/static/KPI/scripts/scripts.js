function ajaxSend(url, params) {
    // Отправляем запрос
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
}

const forms = document.querySelector('form[name=filter]');

forms.addEventListener('submit', function (e) {
    // Получаем данные из формы
    e.preventDefault();
    let url = this.action;
    let params = new URLSearchParams(new FormData(this)).toString();
    ajaxSend(url, params);
});

function render(data) {
    // Рендер шаблона
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('.left-ads-display>.row');
    div.innerHTML = output;
}

let html = '\
{{#KPI}}\
     <tr>\
                <td class="fio">{{ KPI.employee }}</td>\
                <td class="position">{{ KPI.position }}</td>\
                <td class="kpi">\
                    <div class="tdRow">\
                        <div>{{ KPI.final_coefficient }}%</div>\
                        <div><a href="final/{{ KPI.pk }}"><i class="far fa-list-alt"></i></a></div>\
                    </div>\
                </td>\
                    <td class="kpi">\
                    <div class="tdRow">\
                        <div>{{ KPI.plan_сoefficient }}%</div>\
                        <div><a href="plan/{{ KPI.pk }}"><i class="far fa-list-alt"></i></a></div>\
                    </div>\
                </td>\
                <td class="kpi">\
                    <div class="tdRow">\
                        <div>{{ KPI.quality_сoefficient }}%</div>\
                        <div><a href="quality/{{ KPI.pk }}/"><i class="far fa-list-alt"></i></a></div>\
                    </div>\
                </td>\
                <td class="change"><i class="fas fa-edit"></i></td>\
                <td class="change"><i class="fas fa-trash-alt"></i></td>\
            </tr>\
{{/KPI}}'