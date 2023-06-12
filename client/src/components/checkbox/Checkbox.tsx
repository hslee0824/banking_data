interface CheckboxProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
}

export const Checkbox = ({ label, ...rest }: CheckboxProps) => {
  return (
    <div>
      <input type="checkbox" id={`checkbox-${label}`} {...rest} />
      <label className="ml-2" htmlFor={`checkbox-${label}`}>
        {label}
      </label>
    </div>
  );
};

export default Checkbox;
