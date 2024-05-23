import { useEffect, useState } from "react";
import { getAllStations } from "../api/stations.api";
import { StationCard } from "./StationCard";

export function StationList() {
    const [stations, setStations] = useState([]);
    useEffect(() => {
        async function loadStations() {
            const res = await getAllStations();
            setStations(res.data);
        }
        loadStations();
    }, [])
    return (
        <div className="row">
            {stations.map(station => (
                <div key={station.id} className="col-md-4 mb-4">
                    <StationCard station={station} />
                </div>
            ))}
        </div>
    )
}