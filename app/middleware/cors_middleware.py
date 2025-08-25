from fastapi import Request
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware
import logging

logger = logging.getLogger(__name__)

class CORSDebugMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Log de la petición entrante
        logger.info(f"CORS Debug: {request.method} {request.url}")
        logger.info(f"CORS Debug: Origin: {request.headers.get('origin')}")
        logger.info(f"CORS Debug: User-Agent: {request.headers.get('user-agent')}")
        
        # Continuar con la petición
        response = await call_next(request)
        
        # Log de la respuesta
        logger.info(f"CORS Debug: Response status: {response.status_code}")
        logger.info(f"CORS Debug: CORS headers: {dict(response.headers)}")
        
        return response
