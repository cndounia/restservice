from hostingPackage import hostingModule
from api_controllers import api


app = hostingModule.getApplication()
api.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=45000, debug=True)
