import { useForm } from 'react-hook-form';
import { createPatient } from '../api/patients.api';
import { useNavigate } from 'react-router-dom';

export function PatientsForm(){
    const {
        register, 
        handleSubmit,
        formState: { errors }
    } = useForm()

    const navigate = useNavigate();
    
    const onSubmit = handleSubmit(async data => {
        await createPatient(data);
        navigate('/patients')
    })

    return (
        <div className="container">
            <h1 className="mb-4">Create Patient</h1>
            <form onSubmit={onSubmit} className="needs-validation">
                <div className="mb-3">
                    <label className="form-label">Full Name</label>
                    <input
                        type="text"
                        className={`form-control ${errors.full_name ? 'is-invalid' : ''}`}
                        placeholder="Full Name"
                        {...register("full_name", { required: true })}
                    />
                    {errors.full_name && <div className="invalid-feedback">This field is required</div>}
                </div>
                <div className="mb-3">
                    <label className="form-label">Birth Date</label>
                    <input
                        type="date"
                        className={`form-control ${errors.birth_date ? 'is-invalid' : ''}`}
                        placeholder="Birth Date"
                        {...register("birth_date", { required: true })}
                    />
                    {errors.birth_date && <div className="invalid-feedback">This field is required</div>}
                </div>
                <div className="mb-3">
                    <label className="form-label">Phone Number</label>
                    <input
                        type="tel"
                        className={`form-control ${errors.phone_number ? 'is-invalid' : ''}`}
                        placeholder="Phone Number"
                        {...register("phone_number", { required: true })}
                    />
                    {errors.phone_number && <div className="invalid-feedback">This field is required</div>}
                </div>
                <button type="submit" className="btn btn-primary">Save</button>
            </form>
        </div>
    )
}