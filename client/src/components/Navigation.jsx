import { Link } from "react-router-dom";

export function Navigation() {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container-fluid">
                <Link to="/patients" className="navbar-brand">Patients</Link>
                <div className="collapse navbar-collapse">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                        <li className="nav-item">
                            <Link to="/create-patient" className="nav-link">Create Patient</Link>
                        </li>
                    </ul>
                </div>
                <div className="collapse navbar-collapse">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                        <li className="nav-item">
                            <Link to="/stations" className="nav-link">Stations</Link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    )
}