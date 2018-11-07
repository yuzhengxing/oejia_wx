# -*- coding: utf-8 -*-

{
    'name': 'WeChat',
    'version': '1.0.0',
    'category': 'Social Network',
    'summary': '企业微信公众号的接入与管理',
    'author': 'Oejia',
    'website': 'http://www.oejia.net/',
    'application': True,
    'data': [
             'security/res_groups.xml',
             'security/ir.model.access.csv',
             'data/wx_init_data.xml',
             'views/parent_menus.xml',

             'views/wx_action_act_article_views.xml',
             'views/wx_action_act_custom_views.xml',
             'views/wx_action_act_text_views.xml',
             'views/wx_articlesreply_article_views.xml',
             'views/wx_autoreply_views.xml',
             'views/wx_config_settings_views.xml',
             'views/wx_menu_item_left_views.xml',
             'views/wx_menu_item_middle_views.xml',
             'views/wx_menu_item_right_views.xml',
             'views/wx_menu_views.xml',
             'views/wx_user_group_views.xml',
             'views/wx_user_views.xml',
             'views/wx_config_corpsettings_views.xml',
             'views/wx_corpuser_views.xml',
             'views/wx_confirm_views.xml',
             'views/wx_app_config_views.xml',

             'views/res_partner_views.xml',
             ],
    'qweb': [
    ],
    'depends' : ['web','im_livechat'],
    'installable': True,
    'active': False,
    'web': True,
}
