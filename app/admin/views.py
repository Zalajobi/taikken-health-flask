from app.admin import admin_blueprint


@admin_blueprint.route('/provider/register', methods=['POST'])
def admin_create_provider():
    pass
