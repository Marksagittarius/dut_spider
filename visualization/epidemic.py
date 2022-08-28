from store import get_epidemic_data, register_router
from .basic import Router, height, width
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Map, Bar


source_data = []
router_list = Router()


def render_map_of_current_confirmed_num():
    province_name = []
    data = []

    for province in source_data:
        province_name.append(province.province_name)
        data.append(province.current_confirmed_num)

    map = (
        Map(init_opts=opts.InitOpts(width=width,
            height=height, theme=ThemeType.LIGHT))
        .add("确诊病例", [list(z) for z in zip(province_name, data)])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Confirmed Cases", subtitle="确诊病例分布 (病例数)", pos_top="5%"),
            toolbox_opts=opts.ToolboxOpts(
                is_show=True, pos_left="20%", pos_bottom="5%"),
            visualmap_opts=opts.VisualMapOpts(
                min_=0,
                max_=10000,
                range_text=["High", "Low"],
                is_calculable=True,
                range_color=["rgb(255, 143, 177)",
                             "rgb(178, 112, 162)", "rgb(122, 68, 149)"],
            )
        )

    )

    map.render("static/charts/epidemic/current_confirmed_case_map.html")
    router_list.append_router("current_confirmed_case_map")


def render_map_of_total_local_confirmed_num():
    province_name = []
    data = []

    for province in source_data:
        province_name.append(province.province_name)
        data.append(province.total_local_confirmed_cases)

    map = (
        Map(init_opts=opts.InitOpts(width=width,
            height=height, theme=ThemeType.LIGHT))
        .add("累计确诊病例", [list(z) for z in zip(province_name, data)])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Total Confirmed Cases", subtitle="累计确诊病例分布 (病例数)", pos_top="5%"),
            toolbox_opts=opts.ToolboxOpts(
                is_show=True, pos_left="20%", pos_bottom="5%"),
            visualmap_opts=opts.VisualMapOpts(
                min_=0,
                max_=10000,
                range_text=["High", "Low"],
                is_calculable=True,
                range_color=["rgb(255, 248, 154)",
                             "rgb(255, 178, 166)", "rgb(255, 138, 174)"],
            )
        )

    )

    map.render("static/charts/epidemic/total_local_confirmed_case_map.html")
    router_list.append_router("total_local_confirmed_case_map")


def render_map_of_dead_num():
    province_name = []
    data = []

    for province in source_data:
        province_name.append(province.province_name)
        data.append(province.cumulative_death_roll)

    map = (
        Map(init_opts=opts.InitOpts(width=width,
            height=height, theme=ThemeType.LIGHT))
        .add("累计死亡病例", [list(z) for z in zip(province_name, data)])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Total Dead Cases", subtitle="累计死亡病例分布 (病例数)", pos_top="5%"),
            toolbox_opts=opts.ToolboxOpts(
                is_show=True, pos_left="20%", pos_bottom="5%"),
            visualmap_opts=opts.VisualMapOpts(
                min_=0,
                max_=10000,
                range_text=["High", "Low"],
                is_calculable=True,
                range_color=["rgb(0, 215, 255)",
                             "rgb(0, 150, 255)", "rgb(88, 0, 255)"],
            )
        )

    )

    map.render("static/charts/epidemic/dead_case_map.html")
    router_list.append_router("dead_case_map")


def render_map_of_cured_num():
    province_name = []
    data = []

    for province in source_data:
        province_name.append(province.province_name)
        data.append(province.cumulative_cured_roll)

    map = (
        Map(init_opts=opts.InitOpts(width=width,
            height=height, theme=ThemeType.LIGHT))
        .add("累计治愈病例", [list(z) for z in zip(province_name, data)])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Total Cured Cases", subtitle="累计治愈病例分布 (病例数)", pos_top="5%"),
            toolbox_opts=opts.ToolboxOpts(
                is_show=True, pos_left="20%", pos_bottom="5%"),
            visualmap_opts=opts.VisualMapOpts(
                min_=0,
                max_=10000,
                range_text=["High", "Low"],
                is_calculable=True,
                range_color=["rgb(125, 206, 19)",
                             "rgb(91, 179, 24)", "rgb(43, 122, 11)"],
            )
        )

    )

    map.render("static/charts/epidemic/cured_case_map.html")
    router_list.append_router("cured_case_map")


def render_bar_of_high_danger_num():
    province_name = []
    data = []

    for province in source_data:
        province_name.append(province.province_name)
        data.append(province.high_danger_count)

    bar = Bar(init_opts=opts.InitOpts(width=width, height=height, theme=ThemeType.LIGHT)).add_xaxis(province_name).add_yaxis('', data, is_show_background=True, category_gap="10%").set_global_opts(
        title_opts=opts.TitleOpts(
            title="High Danger", subtitle="高风险地区统计 (地区数)", pos_left="35%"),
        toolbox_opts=opts.ToolboxOpts(
            is_show=True, orient="vertical", pos_left="1%"),
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

    bar.render("static/charts/epidemic/high_danger_bar.html")
    router_list.append_router("high_danger_bar")


def render_bar_of_mid_danger_num():
    province_name = []
    data = []

    for province in source_data:
        province_name.append(province.province_name)
        data.append(province.mid_danger_count)

    bar = Bar(init_opts=opts.InitOpts(width=width, height=height, theme=ThemeType.LIGHT)).add_xaxis(province_name).add_yaxis('', data, is_show_background=True, category_gap="10%").set_global_opts(
        title_opts=opts.TitleOpts(
            title="Middle Danger", subtitle="中风险地区统计 (地区数)", pos_left="35%"),
        toolbox_opts=opts.ToolboxOpts(
            is_show=True, orient="vertical", pos_left="1%"),
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

    bar.render("static/charts/epidemic/mid_danger_bar.html")
    router_list.append_router("mid_danger_bar")


def render_all_about_epidemic():
    """ Rendering all the components of the router "/epidemic".

    """

    print("Render /epidemic")
    router_list.clear()
    global source_data
    source_data = get_epidemic_data()

    render_map_of_current_confirmed_num()
    render_map_of_total_local_confirmed_num()
    render_map_of_dead_num()
    render_map_of_cured_num()
    render_bar_of_high_danger_num()
    render_bar_of_mid_danger_num()
    register_router(router_list, "static/router/epidemic.json")
