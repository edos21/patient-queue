import axios from "axios";

const StationsApi = axios.create({
  baseURL: "http://localhost:8000/patients/v1/stations",
});

export const getAllStations = () => StationsApi.get("/");

export const callNextPatient = async (stationId) => await StationsApi.post(`/${stationId}/next_patient/`)

export const endPatientTurn = async (stationId) => await StationsApi.post(`/${stationId}/end_turn/`)