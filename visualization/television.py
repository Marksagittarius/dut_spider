from store import get_actor_stat, register_router, get_audience_form
from pyecharts.charts import Pie, Bar, Line
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from .basic import Router, height, width, pos_top


source_data = []
audience_form = get_audience_form()

router_list = Router()


def render_pie_of_height():
    height_stat = {}
    cate = []
    data = []
    for actress in source_data:
        if actress.height in height_stat:
            height_stat[actress.height] += 1
        else:
            height_stat[actress.height] = 1

    for key in height_stat:
        cate.append(key)
        data.append(height_stat[key])

    pie = Pie(init_opts=opts.InitOpts(width=width, height=height, theme=ThemeType.LIGHT)).add("", [list(z) for z in zip(cate, data)], radius="70%").set_global_opts(
        title_opts=opts.TitleOpts(
            title="Height", subtitle="演员身高分布 (cm)", pos_top=pos_top),
        toolbox_opts=opts.ToolboxOpts(is_show=True, pos_top="10%")
    )
    pie.render("static/charts/television/height_pie.html")
    router_list.append_router("height_pie")


def render_pie_of_weight():
    weight_stat = {}
    cate = []
    data = []
    for actress in source_data:
        if actress.weight in weight_stat:
            weight_stat[actress.weight] += 1
        else:
            weight_stat[actress.weight] = 1

    for key in weight_stat:
        cate.append(key)
        data.append(weight_stat[key])

    pie = Pie(init_opts=opts.InitOpts(width=width, height=height, theme=ThemeType.LIGHT)).add("", [list(z) for z in zip(cate, data)], rosetype="area", radius="77%").set_global_opts(
        title_opts=opts.TitleOpts(
            title="Weight", subtitle="演员体重分布 (kg)", pos_top=pos_top),
        toolbox_opts=opts.ToolboxOpts(is_show=True, pos_top="10%")
    )
    pie.render("static/charts/television/weight_pie.html")
    router_list.append_router("weight_pie")


def render_pie_of_nation():
    nation_stat = {}
    cate = []
    data = []
    for actress in source_data:
        if actress.nation in nation_stat:
            nation_stat[actress.nation] += 1
        else:
            nation_stat[actress.nation] = 1

    for key in nation_stat:
        cate.append(key)
        data.append(nation_stat[key])

    pie = Pie(init_opts=opts.InitOpts(width=width, height=height, theme=ThemeType.LIGHT)).add("", [list(z) for z in zip(cate, data)], radius=["25%", "70%"]).set_global_opts(
        title_opts=opts.TitleOpts(
            title="Nation", subtitle="演员民族分布 (人数)", pos_top=pos_top),
        toolbox_opts=opts.ToolboxOpts(is_show=True)
    )
    pie.render("static/charts/television/nation_pie.html")
    router_list.append_router("nation_pie")


def render_bar_of_blood_type():
    blood_type_stat = {}
    cate = []
    data = []
    for actress in source_data:
        if actress.blood_type in blood_type_stat:
            blood_type_stat[actress.blood_type] += 1
        else:
            blood_type_stat[actress.blood_type] = 1

    for key in blood_type_stat:
        cate.append(key)
        data.append(blood_type_stat[key])

    bar = Bar(init_opts=opts.InitOpts(width=width, height=height, theme=ThemeType.LIGHT)).add_xaxis(cate).add_yaxis('', data, is_show_background=True).set_global_opts(
        title_opts=opts.TitleOpts(
            title="Blood Type", subtitle="演员血型分布 (人数)", pos_left="35%"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, orient="vertical", pos_left="1%"),
    ).set_series_opts(
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="min", name="最小值"),
                opts.MarkLineItem(type_="max", name="最大值"),
                opts.MarkLineItem(type_="average", name="平均值"),
            ]
        )
    )

    bar.render("static/charts/television/blood_type_bar.html")
    router_list.append_router("blood_type_bar")


def render_bar_of_constellation():
    constellation_stat = {}
    cate = []
    data = []
    for actress in source_data:
        if actress.constellation in constellation_stat:
            constellation_stat[actress.constellation] += 1
        else:
            constellation_stat[actress.constellation] = 1

    for key in constellation_stat:
        cate.append(key)
        data.append(constellation_stat[key])

    bar = Bar(init_opts=opts.InitOpts(width=width, height=height, theme=ThemeType.LIGHT)).add_xaxis(cate).add_yaxis('', data, is_show_background=True, category_gap="10%").set_global_opts(
        title_opts=opts.TitleOpts(
            title="Constellation", subtitle="演员星座分布 (人数)", pos_left="35%"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, orient="vertical", pos_left="1%"),
        datazoom_opts=opts.DataZoomOpts()
    ).set_series_opts(
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="min", name="最小值"),
                opts.MarkLineItem(type_="max", name="最大值"),
                opts.MarkLineItem(type_="average", name="平均值"),
            ]
        )
    )

    bar.render("static/charts/television/constellation_bar.html")
    router_list.append_router("constellation_bar")


def render_line_of_audience_rate():
    dates = []
    rate1 = []
    rate2 = []
    for audience_form_unit in audience_form:
        dates.append(audience_form_unit.date)
        rate1.append(audience_form_unit.rate1)
        rate2.append(audience_form_unit.rate2)
    
    line = Line(init_opts=opts.InitOpts(width=width, height=height, theme=ThemeType.LIGHT)).add_xaxis(dates).add_yaxis(series_name="东方卫视CSM59城收视", y_axis=rate1).set_global_opts(
        title_opts=opts.TitleOpts(
            title="Audience Rate", subtitle="两卫视收视率变化及对比 (%)", pos_left="35%", pos_top="7%"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        datazoom_opts=opts.DataZoomOpts()
    ).add_yaxis(series_name="浙江卫视CSM59城收视", y_axis=rate2)
    line.render("static/charts/television/audience_rate_line.html")
    router_list.append_router("audience_rate_line")
    

def render_line_of_audience_share():
    dates = []
    rate1 = []
    rate2 = []
    for audience_form_unit in audience_form:
        dates.append(audience_form_unit.date)
        rate1.append(audience_form_unit.share1)
        rate2.append(audience_form_unit.share2)

    line = Line(init_opts=opts.InitOpts(width=width, height=height, theme=ThemeType.LIGHT)).add_xaxis(dates).add_yaxis(series_name="东方卫视CSM59城收视", y_axis=rate1).set_global_opts(
        title_opts=opts.TitleOpts(
            title="Audience Share", subtitle="两卫视市场占有变化及对比 (%)", pos_left="35%", pos_top="7%"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        datazoom_opts=opts.DataZoomOpts()
    ).add_yaxis(series_name="浙江卫视CSM59城收视", y_axis=rate2)
    line.render("static/charts/television/audience_share_line.html")
    router_list.append_router("audience_share_line")
    
    
def render_all_about_television():
    """ Rendering all the components of the router "/television".

    """
    
    print("Render /television")
    router_list.clear()
    global source_data
    if len(source_data) == 0:
        source_data = get_actor_stat()

    render_pie_of_height()
    render_pie_of_weight()
    render_pie_of_nation()
    render_bar_of_blood_type()
    render_bar_of_constellation()
    render_line_of_audience_rate()
    render_line_of_audience_share()
    register_router(router_list, "static/router/television.json")
    router_list.clear()
