import axios from "axios";

const PatientsApi = axios.create({
  baseURL: "http://localhost:8000/patients/v1/patients",
});

export const getAllPatients = () => PatientsApi.get("/");
export const createPatient = (patient) => PatientsApi.post("/", patient);
