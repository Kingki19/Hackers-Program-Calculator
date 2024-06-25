import streamlit as st

# DATA CLASS
class Program:
  def __init__(self, name, capacity, levels, costs):
    self.name = name
    self.levels = levels
    if len(costs) == 21:
      self.costs = costs
    else:
      self.costs = None
      st.error(f"Program {self.name} has error and it's costs")  
    self.capacity = capacity

  def get_cost(self, level):
    if level in self.levels:
      index = self.levels.index(level)
      return self.costs[index]
    else:
      return None  # atau Anda bisa mengembalikan pesan error atau nilai default
  
  def get_capacity(self):
    return self.capacity
  
  def __repr__(self):
    return f"Unit(name={self.name}, levels={self.levels}, costs={self.costs})"

class AI_Program:
  def __init__(self, name, levels, costs):
    self.name = name
    self.levels = levels
    if len(costs) == 21:
      self.costs = costs
    else:
      self.costs = None
      st.error(f"Program {self.name} has error and it's costs")  

  def get_cost(self, level):
    if level in self.levels:
      index = self.levels.index(level)
      return self.costs[index]
    else:
      return None  # atau Anda bisa mengembalikan pesan error atau nilai default
  
  def __repr__(self):
    return f"Unit(name={self.name}, levels={self.levels}, costs={self.costs})"

# Inisiasi
### TYPE: OFFENSIVE ###
levels_program = list(range(1, 22))
# BEAM CANNON
cost_beam_cannon = [1,2,4,6,8,10,12,
                    14,16,18,20,22,24,26,
                    28,30,34,38,42,46,50]
beam_cannon = Program("Beam Cannon", 1, levels_program, cost_beam_cannon)
# SHURIKEN
cost_shuriken = [2,4,8,12,16,20,24,
                 28,32,36,40,44,48,52,
                 56,60,68,76,84,92,100]
shuriken = Program("Shuriken", 1, levels_program, cost_shuriken)
# WORMS
cost_worms = [5, 10, 20, 30, 40, 50, 60,
              70, 80, 90, 100, 110, 120, 130,
              140, 150, 170, 190, 210, 230, 250]
worms = Program("Worms", 3, levels_program, cost_worms)
# BATTERING RAM
cost_battering_ram = [40, 60, 80, 100, 120, 140, 160,
                      180, 200, 220, 250, 280, 310, 350,
                      400, 450, 500, 550, 600, 650, 700]
battering_ram = Program("Battering Ram", 5, levels_program, cost_worms)
# SHOCKER
cost_shocker = [25, 40, 55, 70, 85, 100, 120,
                140, 160, 180, 200, 220, 250, 280,
                310, 350, 390, 430, 470, 510, 560]
shocker = Program("Shocker", 6, levels_program, cost_shocker)
# BLASTER
cost_blaster = [20,30,40,50,60,70,80,
                100,120,140,160,180,200,220,
                250,280,300,350,400,450,500]
blaster = Program("Blaster", 6, levels_program, cost_blaster)
# KRAKEN
cost_kraken = [60,120,180,240,300,360,420,
               480,540,600,660,720,780,840,
               900,1020,1140,1260,1380,1500,2000]
kraken = Program("Kraken", 7, levels_program, cost_kraken)
# MANIAC
cost_maniac = [200,300,400,500,600,700,800,
               1000,1200,1400,1600,1800,2000,2200,
               2500,2800,3000,3500,4000,4500,5000]
maniac = Program ("Maniac", 15, levels_program, cost_maniac)

### TYPE: DEFENSIVE ###
# ICE WALL 
cost_ice_wall = [8,15,30,60,90, 120, 150,
                 180,210,240,270,300,330,360,
                 390,420,450,510,570,630,690]
ice_wall = Program("ICE Wall", 2, levels_program,cost_ice_wall)
# PROTECTOR
cost_protector = [30, 60, 90, 120, 150, 180, 210,
                  240, 270, 300, 330, 360, 390, 420,
                  450, 510, 570, 630, 690, 750, 1000]
protector = Program("Protector", 4, levels_program, cost_protector)

### TYPE: STEALTH 
# ACCESS
cost_access = [12, 24, 36, 48, 60, 72, 84,
               100, 116, 132, 148, 164, 180, 200,
               220, 240, 260, 280, 300, 320, 350]
access = Program("Access", 1, levels_program, cost_access)
# DATA LEECH
cost_data_leech = [5,10,20,30,40,50,60,
                   70,80,90,100,110,120,130,
                   140, 150, 170, 190, 210, 230, 250]
data_leech = Program("Data Leech", 3, levels_program, cost_data_leech)
# WRAITH
cost_wraith = [100, 200, 300, 400, 500, 600, 700,
               800, 900, 1000, 1100, 1200, 1300, 1400,
               1500, 1600, 1700, 1800, 1900, 2000, 2100]
wraith = Program("Wraith", 5, levels_program, cost_wraith)
# PORTAL
cost_portal = [160, 320, 480, 640, 800, 960, 1120,
               1280, 1440, 1600, 1760, 1920, 2080, 2240,
               2400, 2560, 2720, 2880, 3040, 3200, 3360]
portal = Program("Portal", 10, levels_program, cost_portal)

### TYPE: AI 
# HAWK
cost_hawk = [500,600,650,700,800,830,860,
             900,930,960,1000,1080,1160,1250,
             1330,1410,1500,1625,1750,1875,2000]
hawk = AI_Program("AI Hawk", levels_program, cost_hawk)
# BEETLE
cost_beetle = [700,800,830,860,900,930,960,
               1000,1080,1160,1250,1330,1410,1500,
               1625,1750,1875,2000,2250,2500,2750]
beetle = AI_Program("AI Beetle", levels_program, cost_beetle)
# SQUID
cost_squid = [250, 500, 750, 1000,1200,1500,1750,
              2000,2250,2500,2750,3000,3250,3500,
              3750,4000,4250,4500,4750,5000,5250]
squid = AI_Program("AI Squid", levels_program, cost_squid)

# IMAGE LOGO
icon_hackers_game = "assets/images/hackers_logo.jpeg"
full_logo_hackers_game = "assets/images/Hackers_Title_1024.png"
url_hackers_game = "https://hackersthegame.fandom.com/wiki/Hackers_Wikia"
# Image Path
class ImagePath:
  # Offensive Programs
  beam_cannon = "assets/images/beam_cannon.webp"
  shuriken = "assets/images/Shuriken.webp"
  worms = "assets/images/Worms.webp"
  kraken = "assets/images/Kraken.webp"
  shocker = "assets/images/Shock.webp"
  blaster = "assets/images/Blaster.webp"
  battering_ram = "assets/images/Battering_ram.webp"
  maniac = "assets/images/Maniac.webp"
  # Defensive Programs
  ice_wall = "assets/images/Icewall.webp"
  protector = "assets/images/Protector.webp"
  # Stealth Programs
  data_leech = "assets/images/Dataleach.webp"
  access = "assets/images/Access.webp"
  portal = "assets/images/Portal.webp"
  wraith = "assets/images/Wraith.webp"
  # AI
  hawk = "assets/images/Hawk.webp"
  beetle = "assets/images/Beetle.webp"
  squid = "assets/images/Squid.webp"
class CurrentLevel:
  # Offensive Programs
  beam_cannon = 9
  shuriken = 7
  worms = 5
  blaster = 4
  kraken = 2
  battering_ram = 4
  shocker = 5
  maniac = 1
  # Defensive Programs
  ice_wall = 6
  protector = 4
  # Stealth Programs
  access = 7
  data_leech = 7
  wraith = 4
  portal = 2
  # AI
  hawk = 2
  beetle = 2
  squid = 2
def show_AI_programs(
  program_name:str,
  image_path: str,
  current_level: int,
)-> tuple:
  st.image(
    image_path,
    caption=program_name,
    use_column_width="auto"
  )
  program_level = st.number_input(
    f"Your {program_name} level",
    min_value=1,
    max_value=21,
    value=current_level,
    step=1,
    key=f"{program_name}_level"
  )
  use_program = st.toggle(
    f"Use {program_name}",
    key=f"use_{program_name}"
  )
  return program_level, use_program

def show_programs(
  program_name:str,
  image_path: str,
  current_level: int,
  disk_space_usage: int,
)-> tuple:
  st.image(
    image_path,
    caption=program_name,
    use_column_width="auto"
  )
  program_level = st.number_input(
    f"Your level",
    min_value=1,
    max_value=21,
    value=current_level,
    step=1,
    key=f"{program_name}_level"
  )
  total_use_program = st.number_input(
    f"Use {program_name}",
    help=f"{program_name} require {disk_space_usage} space",
    min_value=0,
    step=1,
    value=0,
    key=f"total_{program_name}"
    )
  return program_level, total_use_program

# def calculate_capacity(current_capacity, total_capacity):

if "current_capacity" not in st.session_state:
  st.session_state["current_capacity"] = 0
if "total_cost" not in st.session_state:
  st.session_state["total_cost"] = 0

def main():
  with st.sidebar:
    total_capacity = st.number_input(
      label="Programs Capacity",
      value=165,
      step=5,
      key="total_capacity"
    )
  st.logo(full_logo_hackers_game, link=url_hackers_game, icon_image=icon_hackers_game)
  st.header("Hackers Program's Cost Calculator")
  st.caption("Calculate program's cost without difficulty")

  total_capacity_usage = 0
  total_cost = 0

  def update_capacity_and_cost(program_name, image_path, current_level, get_capacity_func, get_cost_func, total_capacity_usage, total_cost):
    level, total_programs = show_programs(
      program_name=program_name,
      image_path=image_path,
      current_level=current_level,
      disk_space_usage=get_capacity_func()
    )
    capacity_usage = total_programs * get_capacity_func()
    cost = total_programs * get_cost_func(level)
    if total_capacity_usage + capacity_usage <= total_capacity:
      total_capacity_usage += capacity_usage
      total_cost += cost
    else:
      st.warning(f"Adding {program_name} exceeds total capacity. Program not added.")
    return total_capacity_usage, total_cost

  def update_cost_AI_program(program_name, use_program, get_cost_func, total_cost):
    if use_program:
      cost = get_cost_func()
      total_cost += cost
    return total_cost

  with st.expander("Offensive Programs"):
    beam_cannon_col, shuriken_col, worms_col, kraken_col = st.columns(4)
    blaster_col, shocker_col, battering_ram_col, maniac_col = st.columns(4)

    with beam_cannon_col:
      total_capacity_usage, total_cost = update_capacity_and_cost("Beam Cannon", ImagePath.beam_cannon, CurrentLevel.beam_cannon, beam_cannon.get_capacity, beam_cannon.get_cost, total_capacity_usage, total_cost)

    with shuriken_col:
      total_capacity_usage, total_cost = update_capacity_and_cost("Shuriken", ImagePath.shuriken, CurrentLevel.shuriken, shuriken.get_capacity, shuriken.get_cost, total_capacity_usage, total_cost)

    with worms_col:
      total_capacity_usage, total_cost = update_capacity_and_cost("Worms", ImagePath.worms, CurrentLevel.worms, worms.get_capacity, worms.get_cost, total_capacity_usage, total_cost)

    with kraken_col:
      total_capacity_usage, total_cost = update_capacity_and_cost("Kraken", ImagePath.kraken, CurrentLevel.kraken, kraken.get_capacity, kraken.get_cost, total_capacity_usage, total_cost)

    with blaster_col:
      total_capacity_usage, total_cost = update_capacity_and_cost("Blaster", ImagePath.blaster, CurrentLevel.blaster, blaster.get_capacity, blaster.get_cost, total_capacity_usage, total_cost)

    with shocker_col:
      total_capacity_usage, total_cost = update_capacity_and_cost("Shocker", ImagePath.shocker, CurrentLevel.shocker, shocker.get_capacity, shocker.get_cost, total_capacity_usage, total_cost)

    with battering_ram_col:
      total_capacity_usage, total_cost = update_capacity_and_cost("Battering Ram", ImagePath.battering_ram, CurrentLevel.battering_ram, battering_ram.get_capacity, battering_ram.get_cost, total_capacity_usage, total_cost)

    with maniac_col:
      total_capacity_usage, total_cost = update_capacity_and_cost("Maniac", ImagePath.maniac, CurrentLevel.maniac, maniac.get_capacity, maniac.get_cost, total_capacity_usage, total_cost)

  with st.expander("Defensive Programs"):
    ice_wall_col, protector_col = st.columns(2)
    with ice_wall_col:
      total_capacity_usage, total_cost = update_capacity_and_cost("ICE Wall", ImagePath.ice_wall, CurrentLevel.ice_wall, ice_wall.get_capacity, ice_wall.get_cost, total_capacity_usage, total_cost)

    with protector_col:
      total_capacity_usage, total_cost = update_capacity_and_cost("Protector", ImagePath.protector, CurrentLevel.protector, protector.get_capacity, protector.get_cost, total_capacity_usage, total_cost)

  with st.expander("Stealth Programs"):
    access_col, data_leech_col, wraith_col, portal_col = st.columns(4)
    with access_col:
      total_capacity_usage, total_cost = update_capacity_and_cost("Access", ImagePath.access, CurrentLevel.access, access.get_capacity, access.get_cost, total_capacity_usage, total_cost)

    with data_leech_col:
      total_capacity_usage, total_cost = update_capacity_and_cost("Data Leech", ImagePath.data_leech, CurrentLevel.data_leech, data_leech.get_capacity, data_leech.get_cost, total_capacity_usage, total_cost)

    with wraith_col:
      total_capacity_usage, total_cost = update_capacity_and_cost("Wraith", ImagePath.wraith, CurrentLevel.wraith, wraith.get_capacity, wraith.get_cost, total_capacity_usage, total_cost)

    with portal_col:
      total_capacity_usage, total_cost = update_capacity_and_cost("Portal", ImagePath.portal, CurrentLevel.portal, portal.get_capacity, portal.get_cost, total_capacity_usage, total_cost)

  with st.expander("AI Programs"):
    hawk_col, beetle_col, squid_col = st.columns(3)
    with hawk_col:
      hawk_level, use_hawk = show_AI_programs(
        program_name="AI Hawk",
        image_path=ImagePath.hawk,
        current_level=CurrentLevel.hawk
      )
      total_cost = update_cost_AI_program("AI Hawk", use_hawk, lambda: hawk.get_cost(hawk_level), total_cost)
    with beetle_col:
      beetle_level, use_beetle = show_AI_programs(
        program_name="AI Beetle",
        image_path=ImagePath.beetle,
        current_level=CurrentLevel.beetle
      )
      total_cost = update_cost_AI_program("AI Beetle", use_beetle, lambda: beetle.get_cost(beetle_level), total_cost)
    with squid_col:
      squid_level, use_squid = show_AI_programs(
        program_name="AI Squid",
        image_path=ImagePath.squid,
        current_level=CurrentLevel.squid
      )
      total_cost = update_cost_AI_program("AI Squid", use_squid, lambda: squid.get_cost(squid_level), total_cost)

  st.session_state['current_capacity'] = total_capacity_usage
  st.session_state['total_cost'] = total_cost

  with st.sidebar:
    st.markdown(f"**Current Capacity Usage**: {st.session_state.current_capacity} | {total_capacity}")
    st.markdown(f"**Total Cost: {st.session_state.total_cost} Bitcoin**")
  with st.sidebar:
    st.divider()
    st.markdown(
      """
      **I do not own any license of images that i shown on this app. All images belong to the game developer Hackers.** 
      """
    )

    
main()
