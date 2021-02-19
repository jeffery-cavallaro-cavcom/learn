#include "util.h"

#include <chrono>
#include <thread>

void sleep_secs(int secs) {
  std::this_thread::sleep_for(std::chrono::seconds(secs));
}
