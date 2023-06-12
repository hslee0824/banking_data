import React from 'react';

interface PrimaryContainerProps extends React.HTMLAttributes<HTMLDivElement> {
  className?: string;
}

const PrimaryContainer = ({
  children,
  className,
  ...rest
}: PrimaryContainerProps) => {
  return (
    <div
      className={
        'bg-white w-11/12 h-fit p-8 md:p-12 min-w-[320px] md:w-[50vw] shadow-lg rounded-sm overflow-hidden ' +
        className
      }
      {...rest}
    >
      {children}
    </div>
  );
};

export default PrimaryContainer;
