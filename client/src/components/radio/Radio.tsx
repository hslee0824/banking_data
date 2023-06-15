interface RadioProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  chosenValue: string;
}

export const Radio = ({ label, chosenValue, ...rest }: RadioProps) => {
  return (
    <div>
      <input
        type="radio"
        id={`radio-${label}`}
        name={label}
        value={label}
        checked={label === chosenValue}
        {...rest}
      />
      <label className="ml-2" htmlFor={`radio-${label}`}>
        {label}
      </label>
    </div>
  );
};

export default Radio;
