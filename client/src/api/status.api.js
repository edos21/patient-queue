import axios from "axios";

const StationsApi = axios.create({
  baseURL: "http://localhost:8000/patients/v1/status",
});

export const getAllStations = (status) => StationsApi.post("/", status);
