from user_inerface import temperature_view
from user_inerface import wind_speed_view
from user_inerface import pressure_view


def create(device=1):
    xml = '<xml>\n'
    xml += '   <Temperature units = "c">{}</temperature>\n'.format(
        temperature_view(device))
    xml += '   <Wind_speed units = "m/s">{}</wind_speed_view\n'.format(
        wind_speed_view(device))
    xml += '   <Pressure units = "mmHg">{}</pressure>\n'.format(
        pressure_view(device))
    xml += '   </xml>'

    with open('data.xml', 'w') as page:
        page.write(xml)

    return xml


def new_create(data, device=1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n'
    xml += '   <Temperature units = "F">{}</temperature>\n'.format(t)
    xml += '   <Wind_speed units = "m/s">{}</wind_speed_view\n'.format(w)
    xml += '   <Pressure units = "mmHg">{}</pressure>\n'.format(p)
    xml += '   </xml>'

    with open('new_data.xml', 'w') as page:
        page.write(xml)

    return data
