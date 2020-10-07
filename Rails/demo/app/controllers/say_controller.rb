class SayController < ApplicationController
  def hello
    @time = Time.now
    @files = Dir.glob('*')
  end

  def goodbay
    @time = Time.now
  end
end
