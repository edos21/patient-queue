import { useEffect, useState } from "react";
import { getAllStations } from "../api/stations.api";
import { StationCard } from "./StationCard";

export function StationList() {
    const [stations, setStations] = useState([]);
    const loadStations = async () => {
        const res = await getAllStations();
        setStations(res.data);
    };

    useEffect(() => {
        loadStations();
    }, []);
    return (
        <div className="row">
            {stations.map(station => (
                <div key={station.id} className="col-md-4 mb-4">
                    <StationCard station={station} onUpdate={loadStations}/>
                </div>
            ))}
        </div>
    )
}