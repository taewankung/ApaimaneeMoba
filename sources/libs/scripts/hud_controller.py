from bge import logic
from bge import render
import Rasterizer
Rasterizer.showMouse(True)
from libs.apaimanee.menu.menu_scripts.StatusBar import StatusBar
from libs.apaimanee.menu.menu_scripts.hud_camera_controller import HudCamera
from libs.apaimanee.characters.hero.hero import Hero

def run_hud_interface():
    controller = logic.getCurrentController()
    own = controller.owner
    scene = logic.getCurrentScene()
    scene_main = logic.getCurrentScene()
    if scene_main.name != 'main':
            for obj in logic.getSceneList():
                if obj.name == 'main':
                    scene_main = obj                                 
                    camera_main = scene_main.objects['Camera']
                    mouse = controller.sensors["mouse"]
                    hp_bar_obj = scene.objects["hp_bar"]
                    mp_bar_obj = scene.objects["mp_bar"]
                    hud_camera_obj = scene.objects["Hud_camera"]
                    unit = scene_main.objects["sinsamut"]

                    hud_obj_dict = {
                        "hp_bar":hp_bar_obj,
                        "mp_bar":mp_bar_obj,
                        "back_bar":scene.objects["background_bar"],
                        "back_status":scene.objects["background_status"],
                        "image":scene.objects["image"],
                        "exp_bar":scene.objects["exp_bar"],
                        "hero_status":scene.objects["hero_status"],
                        "hero_item":scene.objects["hero_item"],
                        "inside_status":scene.objects["inside_status"],
                        "mini_map":scene.objects["minimap"],
                        "kda_status":scene.objects["kda_status"],
                        "enemy_status":scene.objects["enemy_status"],
                        "text_name_hero":scene.objects["Text_Name_Hero"],
                        "text_hp_bar":scene.objects["Text_hp_bar"],
                        "text_mp_bar":scene.objects["Text_mp_bar"],
                        "text_dmg":scene.objects["Text_dmg"],
                        "text_magic":scene.objects["Text_magic"],
                        "text_armor":scene.objects["Text_armor"],
                        "text_gold":scene.objects["Text_gold"],
                        "camera_main":camera_main
                        }
                    hp_bar = StatusBar(
                        name_act="hp_bar_action",
                        obj_bar = hp_bar_obj,
                        max_value_name = "max_hp",
                        current_value_name = "hp",
                        ghost_value_name="ghost_hp",
                        unit=unit
                        )
                    mp_bar = StatusBar(
                        name_act="mp_bar_action",
                        obj_bar = mp_bar_obj,
                        max_value_name = "max_mp",
                        current_value_name = "mp",
                        ghost_value_name="ghost_mp",
                        unit=unit
                        )
                    hud_camera = HudCamera(controller,hud_camera_obj,unit,hud_obj_dict,speed=1)
                    hud_camera.unit_status()
                    hud_camera.move()
