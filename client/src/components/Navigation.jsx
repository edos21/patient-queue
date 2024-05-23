import { Link } from "react-router-dom";

export function Navigation() {
    return (
        <div>
            <Link to="/patients">
                <p>Patients</p>
            </Link>
            <Link to="/create-patient">Create Patient</Link>
        </div>
    )
}