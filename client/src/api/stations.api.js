import axios from "axios";

const StationsApi = axios.create({
  baseURL: "http://localhost:8000/patients/v1/stations",
});

export const getAllStations = () => StationsApi.get("/");
