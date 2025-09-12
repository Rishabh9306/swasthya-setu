# services/medicine_api/main.py

import logging
from fastapi import FastAPI, HTTPException, Query
from typing import List

# Import your existing, well-tested logic
from .medicine_retriever import (
    retrieve_and_summarize, 
    compare_medicines, 
    requests
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the FastAPI app
app = FastAPI(
    title="Medicine Information API",
    description="An API to fetch and compare medicine information using the RxNorm API.",
    version="1.0.0",
)

@app.get("/", summary="Health Check")
def read_root():
    """A simple health check endpoint to confirm the API is running."""
    return {"status": "ok", "message": "Medicine API is running"}


@app.get("/info", summary="Get Information for a Single Medicine")
def get_medicine_info(name: str = Query(..., description="The brand or generic name of the medicine.")):
    """
    Takes a single medicine name, looks it up, and returns a formatted summary.
    """
    logger.info(f"Received request for medicine info: {name}")
    try:
        summary = retrieve_and_summarize(name)
        if "Sorry, I couldn’t find" in summary:
            # If the retriever gives a fallback, return a standard 404 error
            raise HTTPException(status_code=404, detail=summary)
        return {"summary": summary}
    except requests.exceptions.RequestException as e:
        logger.error(f"Upstream API (RxNorm) error for query '{name}': {e}")
        raise HTTPException(status_code=503, detail="The external medicine database is currently unavailable.")
    except Exception as e:
        logger.error(f"An unexpected error occurred for query '{name}': {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred.")


@app.get("/compare", summary="Compare Two Medicines")
def get_medicine_comparison(
    med1: str = Query(..., description="The first medicine name."),
    med2: str = Query(..., description="The second medicine name.")
):
    """
    Takes two medicine names and returns a formatted comparison summary.
    """
    logger.info(f"Received request to compare: {med1} vs {med2}")
    try:
        comparison = compare_medicines(med1, med2)
        if "Sorry, I couldn't find" in comparison:
            raise HTTPException(status_code=404, detail=comparison)
        return {"summary": comparison}
    except requests.exceptions.RequestException as e:
        logger.error(f"Upstream API (RxNorm) error for comparison '{med1} vs {med2}': {e}")
        raise HTTPException(status_code=503, detail="The external medicine database is currently unavailable.")
    except Exception as e:
        logger.error(f"An unexpected error occurred for comparison '{med1} vs {med2}': {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred.")