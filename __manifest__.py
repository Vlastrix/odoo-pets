# -*- coding: utf-8 -*-
{
    'name': "odoo-pets",

    'summary': """
        Manage and monitor office pets for a harmonious workplace.
        """,

    'description': """
    This module, "Odoo-Pets," is designed to facilitate the management and monitoring of pets in the workplace environment. It is especially beneficial for companies with pet-friendly policies or resident animals on their premises.

    Key Features:
    - Register detailed information about each pet, including their name, species, breed, age, and more.
    - Maintain a photo gallery for each pet.
    - Manage medical information, including vaccinations, allergies, and special conditions.
    - Assign a responsible employee within the company for each pet.

    The module also allows you to schedule and set reminders for pet-related activities, record pet-related events, and designate specific pet areas within the office. You can monitor the health and well-being of pets, track interactions with employees, and even promote pet adoption initiatives. Additionally, it integrates with other modules for a seamless experience.

    With "Odoo-Pets," companies can create a harmonious and organized workplace, ensuring the well-being of both pets and employees. The flexibility of Odoo allows for customization and expansion to meet the specific needs of each organization.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/pet_tree.xml',
        'views/pet_form.xml',
        'views/pet_kanban.xml',
        'views/pet_search.xml',
        'views/pet_species_form.xml',
        'views/pet_species_breed_form.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
