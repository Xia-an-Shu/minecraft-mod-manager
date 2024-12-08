from pathlib import Path
from model.mod import Mod
import json
import os

class ModManager:
    def __init__(self, engine: str = None, version: str = None):        
        self.refresh(engine, version)
    
    def refresh(self, engine: str = None, version: str = None):
        # set engine and version
        if engine is not None and version is not None:
            self.engine = engine
            self.version = version
        else:
            # choose first element from find_all_versions
            versions = self.find_all_versions()
            self.engine = versions[0].split()[0]
            self.version = versions[0].split()[1]
        
        self.mods = []
        self.isready = False
        self.fetch_mods()
        
    def add_mod(self, mod: Mod):
        self.mods.append(mod)
    
    def fetch_mods(self):
        # fetch mods from a file
        try:
             # Build path to correct mods.json
            data_dir = Path('data')
            mods_path = data_dir / self.engine / self.version / 'mods.json'
            
            # Read and parse JSON file
            with open(mods_path, 'r') as f:
                mods_data = json.load(f)
                
                # Create Mod objects from JSON data
                for mod_data in mods_data:
                    mod = Mod(
                        name=mod_data['name'],
                        filename=mod_data['filename'], 
                        url=mod_data['url'],
                        img=mod_data['img'],
                        side=mod_data['side'],
                        active=mod_data['active'],
                        description=mod_data['description'],
                        tags=mod_data['tags'],
                        dependencies=mod_data['dependencies']
                    )
                    self.add_mod(mod)
            self.isready = True
                
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except json.JSONDecodeError:
            print(f"Invalid mods.json file for {self.engine} {self.version}")
            
    def find_all_versions(self):
        # find all versions of a mod
        versions = []
        data_dir = Path('data')
        engines = os.listdir(data_dir)
        for engine in engines:
            for v in os.listdir(data_dir / engine):
                versions.append(f"{engine} {v}")
        return versions