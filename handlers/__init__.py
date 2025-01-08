from handlers.ping import router as ping_router
from handlers.tasks import router as task_router
from handlers.categories import router as categories_router

routers = [task_router, ping_router, categories_router]

