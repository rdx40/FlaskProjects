from jinja2 import Template

grm_daily_awards = [
    {"year": 2020, "awardee": "Stormzy", "category": "Best UK Rap Performance"},
    {"year": 2021, "awardee": "Dave", "category": "Best Lyricist"},
    {"year": 2022, "awardee": "AJ Tracey", "category": "Song of the Year"},
    {"year": 2023, "awardee": "Little Simz", "category": "Album of the Year"},
    {"year": 2024, "awardee": "Skepta", "category": "Lifetime Achievement Award"},
]


TEMPLATE ="""
<!DOCTYPE html>
<head>
        <meta charset="UTF-8"/>
        <title> RATED AWARDS </title>
        <meta name="description" content="This page lists GRM Daily Rated Awardees"/>
</head>
<body>
     <h1> Awardees </h1>
    <table>
        <thead>
            <tr>
              <th>Year</th>
              <th>Awardees</th>
              <th>Language</th>
          </tr>
        </thead>
        <tbody>
            {% for grm in grm_daily_awards %}
            <tr>
                <td>{{ grm["year"] }}</td>
                <td>{{ grm["awardee"] }}</td>
                <td>{{ grm["category"] }}</td>
            </tr>
            {% endfor %}
          </tr>
        </tbody>
    </table>                    
</body>
</html>
"""

template = Template(TEMPLATE)
print(template.render(grm_daily_awards=grm_daily_awards))
my_html_document_file = open('grm.html', 'w')
my_html_document_file.write(template.render(grm_daily_awards=grm_daily_awards))
my_html_document_file.close()