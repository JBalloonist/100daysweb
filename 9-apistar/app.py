from apistar import App, Route, types, validators
from apistar.http import JSONResponse

def list_cars():
	return 'Here are some cars.'

routes = [
    Route('/', method='GET', handler=list_cars),
    # Route('/', method='POST', handler=create_car),
    # Route('/{car_id}/', method='GET', handler=get_car),
    # Route('/{car_id}/', method='PUT', handler=update_car),
    # Route('/{car_id}/', method='DELETE', handler=delete_car),
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)