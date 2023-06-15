import React, { useState } from 'react';
import { Slider } from '../components/slider/Slider';
import SliderWrapper from '../components/slider/SliderWrapper';

const Page2 = () => {
  const sliderDefaultValue = [33];
  const [sliderValue, setSliderValue] = useState(sliderDefaultValue);
  const sliderValueRange = [0, 100];

  return (
    <div>
      <SliderWrapper
        name="Something"
        value={sliderValue}
        min={sliderValueRange[0]}
        max={sliderValueRange[1]}
      >
        <Slider
          defaultValue={sliderDefaultValue}
          min={sliderValueRange[0]}
          max={sliderValueRange[1]}
          step={1}
          onValueChange={(e) => setSliderValue(e)}
          value={sliderValue}
        />
      </SliderWrapper>
    </div>
  );
};

export default Page2;
