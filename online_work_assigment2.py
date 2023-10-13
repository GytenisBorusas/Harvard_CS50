"""
Prompt
Can you re-write this code making improvements to any sections, e.g. from a readability, 
performance, functionality, or neatness perspective? Explain your suggestions.



def get_full_materials_endpoint(
 tenant_name: str,
 material_set_id: int,
 material_physics_set_id: int,
 material_chemistry_set_id: int,
 request: Request, # noqa: ARG001
 session: Session = Depends(get_db),
) -> List[api_schema.MaterialPropertiesView]:
 materials: List[db_schema.Material] = (
 session.scalars(
 sa.select(db_schema.Material)
 .join(db_schema.MaterialSetItem)
 .join(db_schema.MaterialChemistry)
 .join(db_schema.MaterialPhysics)
 .join(db_schema.ChemicalElement)
 .options(
 contains_eager(db_schema.Material.material_chemistry_items),
 contains_eager(db_schema.Material.material_physics_items),
 )
 .where(db_schema.MaterialSetItem.material_set_id == material_set_id)
 .where(
 db_schema.MaterialPhysics.material_physics_set_id
 == material_physics_set_id
 )
 .where(
 db_schema.MaterialChemistry.material_chemistry_set_id
 == material_chemistry_set_id
 )
 .where(db_schema.Material.tenant_name == tenant_name)
 .order_by(db_schema.Material.id)
 )
 .unique()
 .fetchall()
 )

 
 def variability(element: str, scale: float) -> api_schema.Variability:
 if scale == 0:
 return None
 elif scale < LOW_VARIABILITY[element]:
 return "low"
 elif scale < MEDIUM_VARIABILITY[element]:
 return "medium"
 else:
 return "high"


 result = []



 for material in materials:
 elements = {}
 for chemistry in material.material_chemistry_items:
 name = chemistry.chemical_element.name
 elements[name] = ElementPropertiesView(
 mean=chemistry.loc, variability=variability(name, chemistry.scale)
 )
 if len(material.material_physics_items) > 1:
 logging.warning(
 f"Found more than one material physics for {material.id=} in "
 f"{material_physics_set_id=}. Taking first element."
 )
 physics = material.material_physics_items[0]
 view = api_schema.MaterialPropertiesView(
 material_id=material.id,
 material_name=material.name,
 material_type=material.material_type,
 yield_percent=physics.yield_percent,
 density=physics.density,
 min_feasible_mass=physics.min_feasible_mass,
 element_statistics=elements,
 )
 result.append(view)


 return result
"""



